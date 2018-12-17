import { OnDestroy, OnInit, Component, ChangeDetectorRef } from "@angular/core";
import { FormBuilder, Validators } from "@angular/forms";
import { WebAngularDataStore } from "@webdjangular/core/services";
import { NbToastrService } from "@nebular/theme";
import { Subscription, Observable } from "rxjs";
import { AbstractModel } from "@webdjangular/core/data-models";
import { JsonApiModel, JsonApiQueryData } from "angular2-jsonapi";
import { HttpClient, HttpResponse, HttpHeaders, HttpRequest, HttpHandler, HttpEvent } from "@angular/common/http";
import { HttpParamsOptions, HttpParams } from "@angular/common/http/src/params";
import { tap } from "rxjs/operators";
import { MediaModel } from "libs/core/media/src/lib/models/Media.model";

@Component({
  selector: 'wda-export-import',
  styleUrls: ['./export-import.component.scss'],
  templateUrl: 'export-import.component.html'
})
export class AdminExportImportComponent implements OnInit, OnDestroy {

  formGroup = this.fb.group({
    file: [null, Validators.required],
    model: [null, Validators.required],
  });
  public options = [];
  private models = [];
  public loading = true;
  public loading_percentage = 0;
  public loading_text: string = null;
  public data = [];
  public subscription: Subscription;
  public uploadedFiles = {}
  constructor(
    private fb: FormBuilder,
    private cd: ChangeDetectorRef,
    private datastore: WebAngularDataStore,
    private toaster: NbToastrService,
  ) { }

  onFileChange(event) {
    const reader = new FileReader();

    if (event.target.files && event.target.files.length) {
      const [file] = event.target.files;
      reader.readAsText(file);

      reader.onload = () => {
        this.formGroup.patchValue({
          file: reader.result
        });
        try {
          this.data = JSON.parse(reader.result as string);
        } catch (error) {
          this.toaster.danger(`Error Invalid File, Details: ${error}`, `Error!`, { duration: 5000 });
        }
        // need to run CD since file load runs outside of zone
        this.cd.markForCheck();

      };
    }
  }
  onSubmit(event) {
    if (this.formGroup.get('model').value && this.models[this.formGroup.get('model').value]) {
      this.loadRecursive(this.formGroup.get('model').value);
    }
    //this.toaster.success(`Changes have been saved`, `Success!`);
  }
  onChange(event) {
  }
  ngOnInit() {
    this.models = Reflect.getMetadata('JsonApiDatastoreConfig', this.datastore.constructor).models;
    for (const key in this.models) {
      if (this.models.hasOwnProperty(key)) {
        this.options.push({ 'value': key, 'label': key });

      }
    }
    this.loading = false;
  }
  ngOnDestroy() {
    if (this.subscription) {
      this.subscription.unsubscribe();
    }
  }

  private getDataRelationship(model, data): Promise<AbstractModel> {
    let promises: Promise<boolean>[] = [];

    const entry = this.datastore.createRecord(model) as AbstractModel;

    for (const key in data) {
      if (data.hasOwnProperty(key)) {
        // Let's check if theres a . in the middle to run Link or Download FUnctions
        if (key.search(/\./) >= 0) {
          let keys = key.split(/\./);
          if (keys[0] && keys[1]) {
            if (keys[1] === 'download') {
              // Let's Download the File
              let promise: Promise<boolean> = new Promise((resolve, reject) => {
                  if(this.uploadedFiles.hasOwnProperty(data[key])){
                    entry[keys[0]] = this.uploadedFiles[data[key]]
                    resolve(true);

                  }else{
                    let newMedia = this.datastore.createRecord(MediaModel, {file:data[key]});
                    newMedia.save().subscribe((media: any) =>{
                      entry[keys[0]] = media.safeFileUrl;
                      this.uploadedFiles[data[key]] = media.safeFileUrl;
                      resolve(true);
                    });
                  }

              })
              promises.push(promise);
            } else if (entry.extraOptions[keys[0]].model) {
              const relationshipModel = entry.extraOptions[keys[0]].model;
              let belongsTo = entry.belongTo.find((en: any) => en.propertyName == keys[0]);
              if (belongsTo) {
                let options = {
                  page: { size: 1, number: 1 },
                }
                options[keys[1]] = data[key];
                let promise: Promise<boolean> = new Promise((resolve, reject) => {
                  this.datastore.findAll(relationshipModel, options).subscribe(
                    (response: JsonApiQueryData<any>) => {
                      let entries = response.getModels();
                      if (entries[0]) {
                        if (entries[0][keys[1]] === data[key]) {
                          entry[keys[0]] = entries[0]
                          resolve(true);
                        } else {
                          reject("Not found the Correct Relationship");
                        }

                      }
                    },
                    (error: any) => {
                      reject(error);
                    }
                  );
                })
                promises.push(promise);
                continue;
              }
              let hasMany = entry.hasMany.find((en: any) => en.propertyName == keys[0]);
              if (hasMany) {
                let options = {
                  page: { size: 1, number: 1 },
                }
                options[`${keys[1]}__in`] = data[key].join(",")
                let promise: Promise<boolean> = new Promise((resolve, reject) => {
                  this.datastore.findAll(relationshipModel, options).subscribe(
                    (response: JsonApiQueryData<any>) => {
                      let entries = response.getModels();
                      if (entries.length > 0) {
                        entry[keys[0]] = entries;
                      }
                      resolve(true);
                    },
                    (error: any) => {
                      reject(error);
                    }
                  );
                });
                promises.push(promise);
              }
            }
          }
        }else{
          if (data[key] instanceof Array) {
            if(data[key].length > 0){
              entry[key] = data[key];
            }else{
              entry[key] = new Array();
            }
          }else{
            entry[key] = data[key].toString('utf8');
          }
        }
      }
    }
    return Promise.all(promises)
      .then((results: boolean[]) => {
        return entry;
      })
  }


  private loadRecursive(model_name: string, index = 1) {
    this.loading_percentage = (index * 100) / this.data.length;
    this.loading_text = `${index}/${this.data.length}`;
    this.loading = true;
    let model = this.models[model_name];

    this.getDataRelationship(model, this.data[index - 1]).then((entry) => {
      let options = {}
      if (model.include) {
        options['include'] = model.include;
      }
      let headers = new HttpHeaders({

      })

      this.subscription = entry.save(options,headers).subscribe(
        (model) => {
          if (index >= this.data.length) {
            this.loading = false;
            this.toaster.success(`All Record Saved with Success`, `Success!`);
          } else {
            index++;
            this.loadRecursive(model_name, index);
          }
        },
        (error) => {
          this.loading = false;
          if (error.errors && error.errors.length > 0) {
            for (let i = 0; i < error.errors.length; i++) {
              // TODO: Check pointer to see if is for an specific field and set an error inside the field
              const element = error.errors[i];
              this.toaster.danger(`Error saving the Changes, Details: ${element.detail}`, `Error!`, { duration: 5000 });
            }
          } else {
            this.toaster.danger(`Error saving the Changes`, `Error!`);
          }
        });
    });

    return;

  }
}
