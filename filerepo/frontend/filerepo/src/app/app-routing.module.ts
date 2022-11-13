import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import {HomeComponent} from "./home/home.component";
import {DeleteComponent} from "./delete/delete.component";
import {ListComponent} from "./list/list.component";
import {UploadComponent} from "./upload/upload.component";

const routes: Routes = [
  {path: '/home', component:HomeComponent},
  {path: '', component: HomeComponent},
  {path: '/list', component: ListComponent},
  {path: '/delete', component: DeleteComponent},
  {path: '/upload', component: UploadComponent},
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
