import { Component, OnInit,TemplateRef } from '@angular/core';
import { ActivatedRoute } from '@angular/router';
import { Location } from '@angular/common';
import { FormControl, FormGroup, Validators } from '@angular/forms';
import { BsModalService, BsModalRef } from 'ngx-bootstrap/modal';
 
import { Clip } from '../services/clip/clip';
import { ClipService } from '../services/clip/clip.service';
import { AuthService} from '../services/auth/auth.service'
import { MultimediaDetailComponent } from '../multimedia-detail/multimedia-detail.component'


@Component({
  selector: 'app-clips',
  templateUrl: './clips.component.html',
  styleUrls: ['./clips.component.css']
})
export class ClipsComponent implements OnInit {

  clips: Clip[];
  closeResult: string;
  public addClipForm: FormGroup;
  modalRef: BsModalRef;
  userEmail: String;

  constructor(
    private route: ActivatedRoute,
    private clipService: ClipService,
    private location: Location,
    private auth: AuthService,
    private multi: MultimediaDetailComponent,
    private modalService: BsModalService
  ) {}

  ngOnInit(): void {
   this.clipService.clearClip()
   this.getClips();
   this.getEmail();

   this.addClipForm = new FormGroup({
      name: new FormControl(),
      segIni: new FormControl(),
      segFin: new FormControl()
   });

  }

  openModal(template: TemplateRef<any>) {
    this.addClip();
    this.modalRef = this.modalService.show(template);
  }
   
  getClips(): void {
    const id = +this.route.snapshot.paramMap.get('id');
    this.clipService.getClips(id)
      .subscribe(clips => this.clips = clips);
  }
  
  playClip(seg_init:String, seg_fin:String): void{
      this.multi.playClipM(seg_init, seg_fin)
  }

  addClip(){
    var result =
      this.clipService.addClip(
      1,
      this.multi.getIdMulti(),
      this.addClipForm.get('name').value,
      this.addClipForm.get('segIni').value,
      this.addClipForm.get('segFin').value);
    this.getClips();
  }

  getEmail() {
    console.log(this.auth.getEmail(1))
    this.userEmail = this.auth.getEmail(1);
  }
}