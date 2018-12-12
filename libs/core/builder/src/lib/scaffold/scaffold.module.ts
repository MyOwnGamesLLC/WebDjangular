import { NgModule } from '@angular/core';
import { Ng2SmartTableModule } from 'ng2-smart-table';
import { ScaffoldRoutingModule } from './scaffold-routing.module';
import { ScaffoldComponent } from './scaffold.component';
import { ScaffoldEditComponent } from './edit/scaffold-edit.component';
import { ReactiveFormsModule } from '@angular/forms';
import { CommonModule } from '@angular/common';
import { ThemeModule } from '@webdjangular/core/admin-theme';
import { BuilderFormModule } from '../builder-form.module';


const COMPONENTS = [
    ScaffoldComponent,
    ScaffoldEditComponent,
];

@NgModule({
  imports: [
    ThemeModule,
    ScaffoldRoutingModule,
    Ng2SmartTableModule,
    ReactiveFormsModule,
    CommonModule,
    BuilderFormModule,
  ],
  declarations: [
    ...COMPONENTS
  ],
  entryComponents: [
  ]
})
export class ScaffoldModule {

}
