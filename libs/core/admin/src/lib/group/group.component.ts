import { Component } from '@angular/core';
import { HttpClient } from '@angular/common/http'
import { Router } from "@angular/router";

import { WebAngularDataStore } from '@webdjangular/core/services';
import { WebAngularSmartTableDataSource } from '@webdjangular/core/data';

import { GroupModel } from '@webdjangular/core/users-models';

@Component({
    selector: 'webdjangular-group',
    styleUrls: ['./group.component.scss'],
    templateUrl: './group.component.html',
})
export class GroupComponent{

    source: WebAngularSmartTableDataSource  = new WebAngularSmartTableDataSource(this.datastore, GroupModel, {
        smartTableSettings: {
            columns: {
                id: {
                    title: 'ID',
                    type: 'number',
                },
                name: {
                    title: 'Name',
                    type: 'string',
                },
            },
        },
        onEditButtonClick: ($event) => {
            this.router.navigate(['admin','group','edit', $event.data.id]);
        },
        onDeleteButtonClick: ($event) => {
            console.log($event);

            this.datastore.deleteRecord(GroupModel, $event.data.pk).subscribe(
                (r) => {
                    this.source.remove($event)
                }
            );
        },
        onCreateButtonClick: () => {
            this.router.navigate(['admin','group','new']);
        }
    });

    constructor(
        private datastore: WebAngularDataStore,
        private router: Router,
    ) {

    }

}
