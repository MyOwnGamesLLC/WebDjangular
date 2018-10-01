import { Component } from '@angular/core';
import { HttpClient } from '@angular/common/http'
import { Router } from "@angular/router";

import { WebAngularDataStore } from '@webdjangular/core/services';
import { WebAngularSmartTableDataSource } from '@webdjangular/core/data';

import { UserModel } from '@webdjangular/core/users-models';

@Component({
    selector: 'webdjangular-user',
    styleUrls: ['./user.component.scss'],
    templateUrl: './user.component.html',
})
export class UserComponent{

    source: WebAngularSmartTableDataSource  = new WebAngularSmartTableDataSource(this.datastore, UserModel, {
        smartTableSettings: {
            columns: {
                id: {
                    title: 'ID',
                    type: 'number',
                },
                first_name: {
                    title: 'First Name',
                    type: 'string',
                },
                last_name: {
                    title: 'Last Name',
                    type: 'string',
                },
                email: {
                    title: 'Email',
                    type: 'string',
                },
            },
        },
        onEditButtonClick: ($event) => {
            this.router.navigate(['admin','user','edit', $event.data.id]);
        },
        onDeleteButtonClick: ($event) => {
            this.datastore.deleteRecord(UserModel, $event.data.pk).subscribe(
                (r) => {
                    this.source.remove($event)
                }
            );
        },
        onCreateButtonClick: () => {
            this.router.navigate(['admin','user','new']);
        }
    });

    constructor(
        private datastore: WebAngularDataStore,
        private router: Router,
    ) {

    }

}
