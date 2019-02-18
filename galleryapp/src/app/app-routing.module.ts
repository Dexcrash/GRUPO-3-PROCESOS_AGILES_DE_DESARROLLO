import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';
import { GalleryComponent }      from './gallery/gallery.component';
import { MultimediaDetailComponent }  from './multimedia-detail/multimedia-detail.component';
import { RegisterComponent }  from './register/register.component'; 


const routes: Routes = [
  {path: '', component: GalleryComponent},
  {path: 'detail/:id', component: MultimediaDetailComponent},
  {path: 'register', component: RegisterComponent},
];


@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
