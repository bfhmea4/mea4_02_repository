import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';
import { NgbModule } from '@ng-bootstrap/ng-bootstrap';
import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { HomeComponent } from './home/home.component';
import { DeleteComponent } from './delete/delete.component';
import { UploadComponent } from './upload/upload.component';
import { ListComponent } from './list/list.component';
import { InfoComponent } from './info/info.component';
import { HttpStatusComponent } from './http-status/http-status.component';


@NgModule({
  declarations: [
    AppComponent,
    HomeComponent,
    DeleteComponent,
    UploadComponent,
    ListComponent,
    InfoComponent,
    HttpStatusComponent,
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    NgbModule
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
