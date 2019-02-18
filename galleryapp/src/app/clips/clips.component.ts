import { Component, OnInit, Input } from '@angular/core';
import { ActivatedRoute } from '@angular/router';
import { Location } from '@angular/common';
import { FormControl, FormGroup, Validators } from '@angular/forms';

import { Clip } from '../services/clip/clip';
import { ClipService } from '../services/clip/clip.service';
import { MultimediaDetailComponent } from '../multimedia-detail/multimedia-detail.component.ts'

@Component({
  selector: 'app-clips',
  templateUrl: './clips.component.html',
  styleUrls: ['./clips.component.css']
})
export class ClipsComponent implements OnInit {

  clips: Clip[];
  closeResult: string;
  private addClipForm: FormGroup;

  constructor(
    private route: ActivatedRoute,
    private clipService: ClipService,
    private location: Location,
    private multimediaComp: MultimediaDetailComponent,
  ) {}

  ngOnInit(): void {
   this.clipService.clearClip()
   this.getClips();

   this.addClipForm = new FormGroup({
      name: new FormControl(),
      segIni: new FormControl(),
      segFin: new FormControl()
   });

  }
   
  getClips(): void {
    const id = +this.route.snapshot.paramMap.get('id');
    this.clipService.getClips(id)
      .subscribe(clips => this.clips = clips);
  }
  
  playClip(seg_init:String, seg_fin:String): void{
      this.multimediaComp.playClipM(seg_init, seg_fin)
  }

  addClip(){
    var result =
      this.clipService.addClip(
      this.addClipForm.get('name').value,

      this.addClipForm.get('segIni').value,
      this.addClipForm.get('segFin').value);
  }
}
