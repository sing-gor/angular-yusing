import { Component, OnInit, Input } from '@angular/core';
import { BlogQuryset, BlogBadges } from 'src/app/models/blog.type';
import { BlogHandlerService } from 'src/app/services/blog-handler.service';

@Component({
  selector: 'app-sidebar-right',
  templateUrl: './sidebar-right.component.html',
  styleUrls: ['./sidebar-right.component.less'],
})
export class SidebarRightComponent implements OnInit {
  @Input() display;
  public categoryData: BlogBadges[];
  public tagData: BlogBadges[];

  constructor(private blogService: BlogHandlerService) {
    // this.items.category = 'django';
    // this.items.tags = 'angular';
    // this.items.page = 1;
    this.blogService.categoriesData.subscribe((Message) => {
      this.categoryData = Message;
    });

    this.blogService.tagsData.subscribe((Message) => {
      this.tagData = Message;
    });
  }

  ngOnInit(): void {}
}
