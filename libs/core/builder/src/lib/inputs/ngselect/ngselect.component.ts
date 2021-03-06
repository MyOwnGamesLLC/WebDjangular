import { Component, OnInit } from '@angular/core';
import {
  BuilderFormField,
  BuilderFormFieldConfig
} from '../../interfaces/form-config.interface';
import { FormGroup, FormControl, FormArray } from '@angular/forms';
import { Subscription } from 'rxjs';
import { AbstractForm } from '@core/data/src/lib/forms';
import { WebAngularDataStore } from '@core/services/src/lib/WebAngularDataStore.service';

@Component({
  selector: 'wda-form-ngselect',
  styleUrls: ['ngselect.component.scss'],
  templateUrl: 'ngselect.component.html'
})
export class BuilderFormNgSelectComponent implements BuilderFormField, OnInit {
  config: BuilderFormFieldConfig;
  group: AbstractForm;
  loading = true;
  options = [];
  placeholder = '';
  models = [];
  subsciption: Subscription;
  /**
   * Creates an instance of scaffold form select component.
   * @param datastore
   */
  constructor(private datastore: WebAngularDataStore) { }
  get isFormGroup(): boolean {
    return this.config.model && this.config.formType == FormGroup;
  }
  addTagPromise(name) {

    return new Promise(resolve => {
      this.loading = true;
      resolve({ id: name, name: name, valid: true });
      this.loading = false;
    });
  }
  /**
   * on init
   */
  ngOnInit() {
    if (!this.config.addTags) {
      this.addTagPromise = null;
    }
    if (this.config.addTags === true) {
      let tags = this.group.get(this.config.name).value;
      for (let i = 0; i < tags.length; i++) {
        const tag = tags[i];
        this.options.push({
          id: tag,
          name: tag
        });
        this.loading = false;
      }
    } else if (this.config.model) {
      if (typeof this.config.model === 'string') {
        const models = Reflect.getMetadata(
          'JsonApiDatastoreConfig',
          this.datastore.constructor
        ).models;
        if (models[this.config.model]) {
          this.config.model = models[this.config.model];
        }
      }
      let query_options: any = {};
      if (this.config.options) {
        query_options = this.config.options;
      }
      query_options.page = { size: 50 };
      query_options.include = this.config.options_include;
      this.datastore
        .findAll(this.config.model, query_options)
        .subscribe(data => {
          this.models = data.getModels();
          this.options = [];
          for (let i = 0; i < this.models.length; i++) {
            const entry = this.models[i];

            this.options.push({
              id: entry.id,
              name: entry.toString()
            });
            this.loading = false;
          }
        });
    } else {
      this.loading = false;
      this.options = this.config.options || [];
    }
    if (this.config.value) {
      this.group.get(this.config.name).setValue(this.config.value);
      this.onChange(this.config.value);
    }
    let sub: Subscription;
    sub = this.group.get(this.config.name).valueChanges.subscribe(value => {
      if (sub) sub.unsubscribe();
      this.onChange(value);
    });
  }

  onChange($event) {
    if ($event) {
      this.placeholder = '';
    } else {
      this.getPlaceHolder();
    }

    this.updateValue($event);
  }
  compareValues(a: any, b: any) {
    return a.id === b;
  }
  updateValue(value: any) {
    if (this.config.formType == FormGroup) {
      const fg = this.group.get(this.config.name) as AbstractForm;

      fg.populateForm(this.models.find(model => model.id == value));
    }
  }

  private getPlaceHolder(): void {
    this.placeholder = this.config.placeholder || 'Select Option';
  }
}
