import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';
import { RouterModule, Routes } from '@angular/router'
import { HttpClientModule } from '@angular/common/http';


import { AppComponent } from './app.component';
import { FileinfoComponent } from './fileinfo/fileinfo.component';
import { FilelistComponent } from './filelist/filelist.component';
import { ActivitylistComponent } from './activitylist/activitylist.component';

const routes: Routes = [
  { path: 'files/:id/info', component: FileinfoComponent  },
  { path: '', component: FilelistComponent  },
  {path: 'activitylist', component: ActivitylistComponent}
]

@NgModule({
  declarations: [
    AppComponent,
    FileinfoComponent,
    FilelistComponent,
    ActivitylistComponent
  ],
  imports: [
    BrowserModule,
    RouterModule.forRoot(routes),
    HttpClientModule,
  ],
//  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
