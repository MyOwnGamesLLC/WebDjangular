import { JsonApiModel } from 'angular2-jsonapi';
import { Observable } from 'rxjs';

import 'reflect-metadata';

export class AbstractModel extends JsonApiModel {
  public static formClassRef = null;
  protected service;

  constructor(_datastore, data?: any) {
    super(_datastore, data);
    this.service = _datastore;
  }



  saveHasMany() {
    let hasManyFields = Reflect.getMetadata('HasMany', this);
    let modelConfig = Reflect.getMetadata(
      'JsonApiModelConfig',
      this.constructor
    );
    let extraOptions = Reflect.getMetadata('ExtraOptions', this);

    return this.service.saveHasManyRelationship(
      hasManyFields,
      modelConfig,
      extraOptions,
      this
    );
  }

  get pk() {
    console.log('Property pk() is not set in the model', this);
    return null;
  }

  set pk(value) {
    console.log('Property pk() is not set in the model', this);
  }
}
