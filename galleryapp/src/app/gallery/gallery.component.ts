import { Component, OnInit } from '@angular/core';
import { Multimedia } from '../services/multimedia/multimedia';
import { MultimediaService } from '../services/multimedia/multimedia.service';
import { DomSanitizer } from '@angular/platform-browser';

@Component({
  selector: 'app-gallery',
  templateUrl: './gallery.component.html',
  styleUrls: ['./gallery.component.css']
})
export class GalleryComponent implements OnInit {

  multimedias: Multimedia[];
  selectedImage: Multimedia;

  constructor(private sanitizer:DomSanitizer, private imageService: MultimediaService) { }

  ngOnInit() {
    this.getImages();
    this.transformUrls();
  }

  getImages(): void {
    this.imageService.getMultimedias()
        .subscribe(multimedias => this.multimedias = multimedias);
  }


  transformUrls(): void{
    for (let mul of this.multimedias){
      mul.url = "" + this.sanitizer.bypassSecurityTrustResourceUrl(mul.url.valueOf());
    }
  }
}
