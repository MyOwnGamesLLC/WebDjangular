import { RouterModule, Routes } from '@angular/router';
import { NgModule } from '@angular/core';

import { AdminComponent } from './admin.component';
import { DashboardComponent } from './dashboard/dashboard.component';
import { PageModel } from '@webdjangular/core/cms-models';

import { PermissionGuard } from '@webdjangular/core/services';
import { ThemeModel } from '@webdjangular/core/data-models';
import { PluginModel } from '@webdjangular/core/data-models';
import { ScaffoldModule } from './scaffold/scaffold.module';
import { GroupModule } from './group/group.module';
import { UserModule } from './user/user.module';

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
				loadChildren: () => UserModule,
			},
			{
				path: 'group',
				loadChildren: () => GroupModule,
			},
			{
				path: 'pages',
				loadChildren: () => ScaffoldModule,
				data: {
					model: PageModel,
					title:"Page",
					path: 'pages'
				}
			},
			{
				path: 'core_themes',
				loadChildren: () => ScaffoldModule,
				data: {
					model: ThemeModel,
					title:"Theme",
					path: 'core_themes'
				}
			},
			{
				path: 'core_plugins',
				loadChildren: () => ScaffoldModule,
				data: {
					model: PluginModel,
					title:"Plugin",
					path: 'core_plugins'
				}
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
