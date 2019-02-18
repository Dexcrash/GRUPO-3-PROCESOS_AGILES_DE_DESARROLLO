import { Component, OnInit, Input } from '@angular/core';
import { ActivatedRoute } from '@angular/router';
import { Location } from '@angular/common';

import { Multimedia } from '../services/multimedia/multimedia';
import { MultimediaService }  from '../services/multimedia/multimedia.service';




@Component({
  selector: 'app-multimedia-detail',
  templateUrl: './multimedia-detail.component.html',
  styleUrls: ['./multimedia-detail.component.css']
})
export class MultimediaDetailComponent implements OnInit {

  @Input() multimedia: Multimedia;

  constructor(
    private route: ActivatedRoute,
    private multimediaService: MultimediaService,
    private location: Location
  ) {}


  ngOnInit(): void {
    this.getMultimedia();
    this.urlOriginal = this.multimedia.url;
  }

  urlMultimedia: String;
  urlOriginal: String;

  getMultimedia(): void {
    const id = +this.route.snapshot.paramMap.get('id');
    this.multimediaService.getMultimedia(id)
      .subscribe(multimedia => this.multimedia = multimedia);
  }
  
  goBack(): void {
    this.location.back();
  }

  playOriginal(){
    this.multimedia.url = this.urlOriginal
  }

  playClipM(seg_init:String, seg_fin:String){
    this.urlMultimedia = this.urlOriginal+"#t="+seg_init+","+seg_fin;
    this.multimedia.url = this.urlMultimedia
  }
 
}
