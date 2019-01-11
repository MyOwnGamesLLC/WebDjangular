import { Attribute, JsonApiModelConfig } from 'angular2-jsonapi';
import { AbstractModel } from '@webdjangular/core/data-models';
import { PermissionModel } from '@webdjangular/core/users-models';
import { ExtraOptions } from '@webdjangular/core/decorator';
import { Validators } from "@angular/forms";
import { SmartTableSettings } from "@webdjangular/core/data";
import { DiscountTypeOptions } from '../interfaces/Discount.interface';

@JsonApiModelConfig({
  type: 'CatalogRule',
  modelEndpointUrl: 'store/discount/catalog-rule',
})
export class CatalogRuleModel extends AbstractModel {
  public static include = null;

  @Attribute()
  id: string;

  @Attribute()
  @ExtraOptions({
    validators: [Validators.required],
    type: 'text',
    label: 'Name',
    wrapper_class: 'col-6',
    placeholder: '',
  })
  name: string;

  @Attribute()
  @ExtraOptions({
    validators: [Validators.required],
    type: 'select',
    label: 'Discount Type',
    wrapper_class: 'col-6',
    placeholder: '',
    options: DiscountTypeOptions
  })
  rule_type: string;

  @Attribute()
  @ExtraOptions({
    validators: [Validators.required],
    type: 'text',
    inputType: 'number',
    label: 'Discount Ammount',
    wrapper_class: 'col-6',
    placeholder: '',
  })
  value: string;

  @Attribute()
  @ExtraOptions({
    validators: [],
    type: 'datepicker',
    inputType: 'datetime-local',
    label: 'Start Date/Time',
    wrapper_class: 'col-6',
    placeholder: '',
  })
  start: Date;

  @Attribute()
  @ExtraOptions({
    validators: [],
    type: 'datepicker',
    inputType: 'datetime-local',
    label: 'End Date/Time',
    wrapper_class: 'col-6',
    placeholder: '',
  })
  end: Date;

  @Attribute()
  @ExtraOptions({
    type: 'switch',
    label: 'Is active',
    wrapper_class: 'col-3',
    value: true,
  })
  is_active: boolean;

  @Attribute()
  @ExtraOptions({
    validators: [],
    type: 'jsonLogic',
    label: 'Apply Rule only if all conditions are true',
  })
  conditions: any;

  @Attribute()
  created: Date;

  @Attribute()
  updated: Date;

  permissions: PermissionModel[];

  get pk() {
    return this.id;
  }

  set pk(value) {

  }

  public static smartTableOptions: SmartTableSettings = {
    columns: {

      name: {
        title: 'Name',
        type: 'text',
      },
      rule_type: {
        title: 'Type',
        type: 'text',
      },
      value: {
        title: 'Value',
        type: 'text',
      },
      is_active: {
        title: 'Active',
        type: 'text',
        valuePrepareFunction: (cell,row) => cell ? 'Yes':'No'
      },
      start: {
        title: 'Start Date/Time:',
        type: 'text',
      },
      end: {
        title: 'End Date/Time',
        type: 'text',
      }
    }
  }

}
