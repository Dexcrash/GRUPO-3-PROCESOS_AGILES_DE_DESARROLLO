import { Component, OnInit } from '@angular/core';
import { Multimedia } from '../services/multimedia/multimedia';
import { MultimediaService } from '../services/multimedia/multimedia.service';

@Component({
  selector: 'app-gallery',
  templateUrl: './gallery.component.html',
  styleUrls: ['./gallery.component.css']
})
export class GalleryComponent implements OnInit {

  multimedias: Multimedia[];

  selectedImage: Multimedia;
  constructor(private imageService: MultimediaService) { }

  ngOnInit() {
    this.getImages();
  }

  getImages(): void {
    this.imageService.getMultimedias()
        .subscribe(multimedias => this.multimedias = multimedias);
  }
}