import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';
import { GalleryComponent }      from './gallery/gallery.component';
import { ImageDetailComponent }  from './image-detail/image-detail.component';
import { RegisterComponent }  from './register/register.component'; 


const routes: Routes = [
  {path: 'gallery', component: GalleryComponent},
  {path: 'detail/:id', component: ImageDetailComponent},
  {path: 'register', component: RegisterComponent},
];


@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
