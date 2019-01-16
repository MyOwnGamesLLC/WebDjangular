import {Injectable} from '@angular/core';
import {DatastoreConfig, JsonApiDatastore, JsonApiDatastoreConfig, JsonApiModel,} from 'angular2-jsonapi';
import { Observable } from 'rxjs';
import { UserModel, GroupModel, PermissionModel } from '@core/users/src/lib/models';
import { PageModel, BlockModel, MenuItemModel, MenuModel } from '@core/cms/src/lib/models';
import { ContentTypeModel, CoreConfigGroupModel, CoreConfigInputModel, CoreConfigModel, AbstractModel } from '@core/data/src/lib/models';
import { CityModel, StreetModel, ResellerModel, CondoModel, ChannelModel } from '@plugins/provider/src/lib/data';
import { PostalCodeRangeModel } from '@plugins/provider/src/lib/data/models/PostalCodeRangeModel';
import { ProductModel } from '@plugins/store/src/lib/data/models/Product.model';
import { ProductTypeModel } from '@plugins/store/src/lib/data/models/ProductType.model';
import { ProductAttributeModel } from '@plugins/store/src/lib/data/models/ProductAttribute.model';
import { ProductAttributeOptionModel } from '@plugins/store/src/lib/data/models/ProductAttributeOption.model';


// tslint:disable-next-line:variable-name

function cleanEmptyRecursive(attribute) {
  if (attribute === '') {
    attribute = null;
  } else if (attribute instanceof JsonApiModel) {
    const index = Object.getOwnPropertySymbols(attribute)[0] as any;
    const attributesMetadata: any = attribute[index];
    attribute = getDirtyAttributes(attributesMetadata);
  } else if (attribute instanceof Array || typeof (attribute) == 'object') {
    for (const i in attribute) {
      if (attribute.hasOwnProperty(i)) {
        attribute[i] = cleanEmptyRecursive(attribute[i]);
      }
    }
  }
  return attribute
}

function getDirtyAttributes(attributesMetadata: any): { string: any } {
  const dirtyData: any = {};

  for (const propertyName in attributesMetadata) {
    if (attributesMetadata.hasOwnProperty(propertyName)) {
      const metadata: any = attributesMetadata[propertyName];

      if (metadata.hasDirtyAttributes) {
        const attributeName = metadata.serializedName != null ? metadata.serializedName : propertyName;
        dirtyData[attributeName] = metadata.serialisationValue ? metadata.serialisationValue : metadata.newValue;
        dirtyData[attributeName] = cleanEmptyRecursive(dirtyData[attributeName]);
      }

    }
  }
  return dirtyData;
}

const config: DatastoreConfig = {
  baseUrl: '/api',
  //TODO: Load all This Dynamic
  models: {
    User: UserModel,
    Group: GroupModel,
    Page: PageModel,
    Block: BlockModel,
    Permission: PermissionModel,
    ContentType: ContentTypeModel,
    CoreConfigGroup: CoreConfigGroupModel,
    CoreConfigInput: CoreConfigInputModel,
    CoreConfig: CoreConfigModel,
    City: CityModel, // Provider
    PostalCodeRange: PostalCodeRangeModel, // Provider
    Street: StreetModel, // Provider
    Reseller: ResellerModel, // Provider
    Condo: CondoModel, // Provider
    Channel: ChannelModel, // Provider
    Product: ProductModel, // Store
    ProductType: ProductTypeModel, // Store
    ProductAttribute: ProductAttributeModel, // Store
    ProductAttributeOption: ProductAttributeOptionModel, // Store
    MenuItem: MenuItemModel,
    Menu: MenuModel,
  },
  //overrides: {
  //  getDirtyAttributes: getDirtyAttributes
  //}
};

@Injectable()
@JsonApiDatastoreConfig(config)
export class WebAngularDataStore extends JsonApiDatastore {
  protected getRelationships(data: any): any {
    let relationships: any;
    for (const key in data) {
      if (data.hasOwnProperty(key)) {
        if (data[key] instanceof AbstractModel) {

          relationships = relationships || {};

          if (data[key].id) {
            relationships[key] = {
              data: this.buildSingleRelationshipData(data[key])
            };
          }
        } else if (data[key] instanceof Array && data[key].length > 0 && this.isValidToManyRelation(data[key])) {

          relationships = relationships || {};

          const relationshipData = data[key]
            .filter((model: AbstractModel) => model.id)
            .map((model: AbstractModel) => this.buildSingleRelationshipData(model));

          relationships[key] = {
            data: relationshipData
          };
        } else if (data[key] instanceof Array && data[key].length <= 0) {
          relationships = relationships || {};
          // Cleaning to Many Relationship
          relationships[key] = {
            data: []
          };
        }
      }
    }
    return relationships;
  }

  /**
   * This Function Cleans the Attributes from the Request and send to the Model
   * For now we don't want to do that, because could have read_only dynamic attributes added to the backend
   * TODO: Improve how we manage Dynamic Attributes
   * @param hasManyFields
   * @param modelConfig
   * @param extraOptions
   * @param model
   */

  saveHasManyRelationship<T extends JsonApiModel>(hasManyFields = [], modelConfig = {}, extraOptions = {}, model: JsonApiModel): Observable<any> {
    return new Observable(observe => {
      for (let i = 0; i < hasManyFields.length; i++) {
        let url = `${modelConfig['type']}/${model.pk}/relationships/${hasManyFields[i].relationship}/`;
        let pointer = [];
        let typeToSend = modelConfig['type'];

        /*
           Check if we don't have a different type in the backend
           That property is the "resource_name" that can be set on the ViewSet
           or in the Model. In the case of updating relationships, the resouce_name
           has to be set in the model, if it is not set, the code will get the model
           name to use as "resource_name". Some models we cannot change, such as Permission and Group
           which are built in Djangos code and there is no way to override those models.
           Because of that we have an additional configuration <backendResourceName> in the angular
           model where we can set this name.
         */
        /*
        if (typeof extraOptions[hasManyFields[i].propertyName]['backendResourceName'] !== 'undefined') {
          typeToSend = extraOptions[hasManyFields[i].propertyName]['backendResourceName'];
        }
        if (typeof model[hasManyFields[i].propertyName] !== 'undefined') {
          for (let j = 0; j < model[hasManyFields[i].propertyName].length; j++) {
            pointer.push({
              id: model[hasManyFields[i].propertyName][j].pk,
              type: typeToSend
            });
          }
        }*/
        let body: any = {
          data: null // TODO: Improve this
        };
        this.http.patch(url, body, {headers: this.buildHttpHeaders()}).subscribe(
          (r) => {
            if (i + 1 == hasManyFields.length) {
              observe.complete();
            } else {
              observe.next(r);
            }
          });
      }
    });
  }

}
