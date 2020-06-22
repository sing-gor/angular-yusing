import { Component, OnInit, Input } from '@angular/core';
import { BlogHandlerService } from 'src/app/services/blog-handler.service';
import { SiteHandlerService } from 'src/app/services/site-handler.service';
import { SiteData } from 'src/app/models/site.type';

@Component({
  selector: 'app-sidebar-left',
  templateUrl: './sidebar-left.component.html',
  styleUrls: ['./sidebar-left.component.less'],
})
export class SidebarLeftComponent implements OnInit {
  @Input() display;
  public items: SiteData;
  constructor(private siteDataService: SiteHandlerService) {
    this.getSiteData();
  }

  ngOnInit(): void {}

  private getSiteData = () => {
    this.siteDataService.getSiteData().subscribe(
      (data) => {
        this.items = data;
      },
      (error) => {
        console.log(error);
      }
    );
  };
}
