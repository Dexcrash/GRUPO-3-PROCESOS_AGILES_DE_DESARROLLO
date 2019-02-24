import { Component, OnInit } from '@angular/core';
import { Multimedia } from '../services/multimedia/multimedia';
import { MultimediaService } from '../services/multimedia/multimedia.service';
import { DomSanitizer } from '@angular/platform-browser';
import { Category } from '../services/categories/category.model'
import { CategoriesService } from '../services/categories/categories.service'
import { Type } from '../services/types/type.model'
import { TypesService } from '../services/types/types.service'


@Component({
  selector: 'app-gallery',
  templateUrl: './gallery.component.html',
  styleUrls: ['./gallery.component.css']
})
export class GalleryComponent implements OnInit {

  multimedias: Multimedia[];
  selectedCategory: number = 0;
  selectedType: number = 0;
  selectedMultimedias: Multimedia[];
  options: Category[];
  types: Type[];
  

  constructor(private sanitizer:DomSanitizer, private imageService: MultimediaService, private categoryService: CategoriesService, private typesService: TypesService) { }

  ngOnInit() {
    this.getImages();
    this.getCategories();
    this.getTypes();
  }

  getImages(): void {
    this.imageService.getMultimedias()
        .subscribe(multimedias => this.multimedias = multimedias);
        this.selectedMultimedias = this.multimedias;
  }
  
  getCategories(): void {
    this.categoryService.getCategories()
        .subscribe(categories => this.options = categories);
        var todos = new Category();
        todos.id = 0;
        todos.name = "Todas";
        this.options.push(todos);
  }

  getTypes(): void {
    this.typesService.getTypes()
        .subscribe(types => this.types = types);
        console.log(this.types)
    var todos = new Type();
    todos.id = 0;
    todos.name = "Todos";
    this.types.push(todos);
  }

  filtrar(): void {

    this.selectedMultimedias = this.multimedias;
    console.log("Selected Before", this.selectedMultimedias)
    if(this.selectedCategory > 0){
      this.selectedMultimedias = this.selectedMultimedias.filter( multi => multi.categoria == this.selectedCategory);
    }

    if(this.selectedType > 0){
      this.selectedMultimedias = this.selectedMultimedias.filter( multi => multi.type == this.selectedType);
    }
  }

  transformUrls(): void{
    for (let mul of this.multimedias){
      mul.url = "" + this.sanitizer.bypassSecurityTrustResourceUrl(mul.url.valueOf());
    }
  }
}
