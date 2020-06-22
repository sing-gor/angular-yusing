import { Component, OnInit, Input } from '@angular/core';

@Component({
  selector: 'app-sidebar-bottom',
  templateUrl: './sidebar-bottom.component.html',
  styleUrls: ['./sidebar-bottom.component.less'],
})
export class SidebarBottomComponent implements OnInit {
  @Input() display;
  constructor() {}

  ngOnInit(): void {}
}
