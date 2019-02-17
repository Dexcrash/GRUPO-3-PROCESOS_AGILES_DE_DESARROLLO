import { Component, OnInit, Input } from '@angular/core';
import { ActivatedRoute } from '@angular/router';
import { Location } from '@angular/common';

import { Clip } from '../services/clip/clip';
import { ClipService } from '../services/clip/clip.service';

@Component({
  selector: 'app-clips',
  templateUrl: './clips.component.html',
  styleUrls: ['./clips.component.css']
})
export class ClipsComponent implements OnInit {

  clips: Clip[];
  closeResult: string;

  constructor(
    private route: ActivatedRoute,
    private clipService: ClipService,
    private location: Location,
  ) {}

  ngOnInit(): void {
    this.getClips();
  }
   
  getClips(): void {
    const id = +this.route.snapshot.paramMap.get('id');
    this.clipService.getClips(id)
      .subscribe(clips => this.clips = clips);
  }
  
  goBack(): void {
    this.location.back();
  }
}