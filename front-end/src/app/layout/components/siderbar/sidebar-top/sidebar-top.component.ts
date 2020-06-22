import { Component, OnInit, Input } from '@angular/core';

@Component({
  selector: 'app-sidebar-top',
  templateUrl: './sidebar-top.component.html',
  styleUrls: ['./sidebar-top.component.less'],
})
export class SidebarTopComponent implements OnInit {
  @Input() display;
  constructor() {}

  ngOnInit(): void {}
}
