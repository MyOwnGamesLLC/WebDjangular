import {
  JsonApiModelConfig,
  Attribute,
  HasMany,
  BelongsTo
} from 'angular2-jsonapi';
import { AbstractModel } from './Abstract.model';
import { CoreWebsiteModel } from './CoreWebsite.model';
import { ExtraOptions } from '@core/decorator/src/lib/ExtraOptions.decorator';
import { PermissionModel } from '@core/users/src/lib/models';

@JsonApiModelConfig({
  type: 'core_config'
})
export class CoreConfigModel extends AbstractModel {

  @Attribute()
  slug: string;

  @Attribute()
  value: any;

  @Attribute()
  created: Date;

  @Attribute()
  updated: Date;

  @BelongsTo()
  @ExtraOptions({
    type: 'select',
    label: 'Core Website',
    wrapper_class: 'col-6',
    model: CoreWebsiteModel,
    backendResourceName: 'CoreWebsite'
  })
  core_website: CoreWebsiteModel;

  permissions: PermissionModel[];

  get pk() {
    return this.slug;
  }

  set pk(value) {}
}
