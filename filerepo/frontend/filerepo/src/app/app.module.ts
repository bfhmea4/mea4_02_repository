import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';
import { RouterModule, Routes } from '@angular/router'
import { HttpClientModule } from '@angular/common/http';


import { AppComponent } from './app.component';
import { FileinfoComponent } from './fileinfo/fileinfo.component';
import { StartPageComponent} from "./startpage/start-page.component";

const routes: Routes = [
  { path: 'files/:id/info', component: FileinfoComponent  },
]

@NgModule({
  declarations: [
    AppComponent,
    FileinfoComponent,
    StartPageComponent
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
