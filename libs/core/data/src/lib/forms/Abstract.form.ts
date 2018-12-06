import { JsonApiModel } from 'angular2-jsonapi';

import { FormGroup, Validators, FormControl, FormArray } from '@angular/forms';

import { BuilderFormFieldConfig } from '@webdjangular/core/builder';

export class AbstractForm extends FormGroup {

  /**
   * Form fields of abstract form
   */
  public formFields = {};

  /**
   * Scaffold fields of abstract form
   */
  public scaffoldFields: BuilderFormFieldConfig[] = [];

  /**
   * Listing table settings of abstract form
   */
  public listingTableSettings = {};

  /**
   * Creates an instance of abstract form.
   */
  public constructor() {
    super({});
  }

  /**
   * Generates form
   */
  public generateForm() {
    for (let propName in this.formFields) {
      if (this.formFields[propName].type == FormArray) {

        this.registerControl(propName, new FormArray([], []));
      } else if (this.formFields[propName].type == FormGroup) {
        if (typeof this.formFields[propName].formClass !== 'undefined') {
          const fb = new this.formFields[propName].formClass();
          fb.generateForm();
          this.registerControl(propName, fb);
        } else {
          this.registerControl(propName, new FormGroup({}));
        }
      } else {
        let validators = [];

        if (typeof this.formFields[propName]['validators'] !== 'undefined') {
          validators = this.formFields[propName]['validators'];
        }

        this.registerControl(propName, new FormControl(null, validators));
      }
    }
  }

  /**
   * Populates form
   * @param [entity]
   */
  public populateForm(entity: JsonApiModel|any = null) {
    for (let propName in this.formFields) {
      // From Array
      if (this.formFields[propName].type == FormArray && typeof entity[propName] !== 'undefined') {
        for (let i = 0; i < entity[propName].length; i++) {
          this.pushToFormArrayAttribute(propName, entity[propName][i]);
        }
      } else {
        if (this.formFields[propName].type == FormGroup && typeof entity[propName] !== 'undefined') {
          let fg = this.get(propName) as AbstractForm;
          fg.populateForm(entity[propName]);
        } else if (typeof entity[propName] !== 'undefined') {
          this.get(propName).setValue(entity[propName], { emitEvent: true });
        }
      }
    }
  }

  /**
   * Updates model
   * @param entity JsonApiModel
   */
  public updateModel(entity: JsonApiModel) {
    let values = this.value;

    for (let propName in values) {
      switch (this.formFields[propName].type) {
        case FormGroup:
          // TODO: Not an Entityd need to be done
          break;
        case FormArray:
          // TODO: If this is an entity this will change
          entity[propName] = this.get(propName).value;
          break
        default:
          entity[propName] = values[propName];
          break;
      }
    }
  }


  /**
   * Forms key
   * @param [formKey]
   * @param [fullArray]
   * @returns attribute has many difference
   */
  public getAttributeHasManyDifference(formKey: string = null, fullArray = []): String[] {
    let diff = [];
    let control = this.get(formKey);
    let hasNot = true;

    fullArray.map(function (item) {
      hasNot = true;
      control.value.map(function (item2) {
        if (item2.pk == item.pk) {
          hasNot = false;
        }
      });

      if (hasNot == true) {
        diff.push(item);
      }
    });

    return diff;
  }

  /**
   * Does entity has relationship
   * @param [formKey]
   * @param [toRelateEntity]
   * @returns
   */
  public doesEntityHasRelationship(formKey: string = null, toRelateEntity = null) {
    let control = this.get(formKey);

    return (
      control.value.filter(function (alreadyRelatedEntity) {
        return alreadyRelatedEntity.pk == toRelateEntity.pk;
      }).length > 0
    );
  }

  /**
   * Checkboxs relation listener
   * @param $event
   * @param [formKey]
   * @param [toRelateEntity]
   */
  public checkboxRelationListener($event, formKey: string = null, toRelateEntity = null) {
    let control = this.get(formKey) as FormArray;

    if ($event.target.checked == false) {
      for (let i = 0; i < control.value.length; i++) {
        if (control.value[i].pk == toRelateEntity.pk) {
          control.removeAt(i);
        }
      }
    } else {
      let fb = new this.formFields[formKey].form();
      fb.generateForm();
      fb.populateForm(toRelateEntity);
      control.push(fb);
    }
  }

  /**
   * Pushs to form array attribute
   * @param [formKey]
   * @param entityToPush
   */
  public pushToFormArrayAttribute(formKey: string = null, entityToPush) {
    if (this.formFields[formKey].type == FormArray) {
      let fa = this.get(formKey) as FormArray;
      let f: AbstractForm;
      if (this.formFields[formKey].formClass) {
        f = new this.formFields[formKey].formClass();
      } else {
        f = new entityToPush.constructor.formClassRef();
      }
      f.generateForm();
      f.populateForm(entityToPush);
      fa.push(f);

    }
  }

  public formArrayRemoveAt(formKey:string = null, index= 1){
    if (this.formFields[formKey].type == FormArray) {
      let fa = this.get(formKey) as FormArray;
      fa.removeAt(index);
    }
  }
  /**
   * Transforming the Group to String for the Scaffold Naming
   */
  public toString = (): string => {
    return `#${this.value.pk}`;
  }
}
