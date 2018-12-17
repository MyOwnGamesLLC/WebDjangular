import { RouterModule, Routes } from '@angular/router';
import { NgModule } from '@angular/core';

import { AdminComponent } from './admin.component';
import { DashboardComponent } from './dashboard/dashboard.component';
import { PageModel } from '@webdjangular/core/cms-models';
import { FormModel } from '@webdjangular/core/forms-models'
import { ThemeModel, CoreWebsiteModel } from '@webdjangular/core/data-models';
import { PluginModel } from '@webdjangular/core/data-models';
import { CoreMediaModule } from '@webdjangular/core/media';

import { CoreConfigGroupModule } from './core-config-group/core-config-group.module';

import { UserModel, GroupModel } from '@webdjangular/core/users-models';
import { PluginStoreAdminModule } from 'libs/plugins/store/src/lib/admin/store-admin.module';
import { ScaffoldModule } from '@webdjangular/core/builder';
import { PluginProviderAdminModule } from 'libs/plugins/provider/src/lib/admin/provider-admin.module';
import { AdminExportImportComponent } from './export-import/export-import.component';


const routes: Routes = [
  {
    path: '',
    component: AdminComponent,
    children: [
      {
        path: '',
        component: DashboardComponent,
      },
      {
        path: 'user',
        loadChildren: () => ScaffoldModule,
        data: {
          model: UserModel,
          title: "Users",
          path: 'user'
        }
      },
      {
        path: 'group',
        loadChildren: () => ScaffoldModule,
        data: {
          model: GroupModel,
          title: "Groups",
          path: 'group'
        }
      },
      {
        path: 'media',
        loadChildren: () => CoreMediaModule,
      },
      {
        path: 'pages',
        loadChildren: () => ScaffoldModule,
        data: {
          model: PageModel,
          title: "Page",
          path: 'pages'
        }
      },
      {
        path: 'forms',
        loadChildren: () => ScaffoldModule,
        data: {
          model: FormModel,
          title: "Form",
          path: 'forms'
        }
      },
      {
        path: 'core_themes',
        loadChildren: () => ScaffoldModule,
        data: {
          model: ThemeModel,
          title: "Theme",
          path: 'core_themes'
        }
      },
      {
        path: 'core_plugins',
        loadChildren: () => ScaffoldModule,
        data: {
          model: PluginModel,
          title: "Plugin",
          path: 'core_plugins'
        }
      },
      {
        path: 'core_websites',
        loadChildren: () => ScaffoldModule,
        data: {
          model: CoreWebsiteModel,
          title: 'Websites',
          path: 'core_websites'
        }
      },

      {
        path: '',
        loadChildren: () => PluginProviderAdminModule,
      },
      {
        path: '',
        loadChildren: () => PluginStoreAdminModule
      },
      {
        path: 'core_config_group/:id',
        loadChildren: () => CoreConfigGroupModule
      },
      {
        path: 'import-export',
        component: AdminExportImportComponent
      }
    ],
  },
];

@NgModule({
  imports: [RouterModule.forChild(routes)],
  exports: [RouterModule],
})
export class AdminRoutingModule {
}
