import { JsonApiModelConfig, Attribute, HasMany, BelongsTo } from 'angular2-jsonapi';

import { AbstractModel } from './Abstract.model';
import { PermissionModel } from './Permission.model';

import { AuthorForm } from '../forms/Author.form';


@JsonApiModelConfig({
    type: 'core_author',
})
export class AuthorModel extends AbstractModel {

	public static formClassRef = AuthorForm;

    @Attribute()
    id: string;

    @Attribute()
    name: string;

    @Attribute()
    email: string;
    
    @Attribute()
    website: string;
    
    @Attribute()
    created: Date;

    @Attribute()
    updated: Date;

    permissions: PermissionModel[]

    get pk(){
    	return this.id;
    }

    set pk(value){
        
	}
}
