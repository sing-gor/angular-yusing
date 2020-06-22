import { Component, OnInit } from '@angular/core';
import { BlogHandlerService } from 'src/app/services/blog-handler.service';
import { Title } from '@angular/platform-browser';
import { BlogList, BlogBadges } from 'src/app/models/blog.type';
import { ActivatedRoute } from '@angular/router';

@Component({
  selector: 'app-blog-list',
  templateUrl: './blog-list.component.html',
  styleUrls: ['./blog-list.component.less'],
})
export class BlogListComponent implements OnInit {
  public pageIndexs: number;
  public items: BlogList;
  public categoryData: BlogBadges[];
  public tagsData: BlogBadges[];
  constructor(
    private blogService: BlogHandlerService,
    private titleService: Title,
    private route: ActivatedRoute
  ) {
    this.route.queryParams.subscribe((params) => {
      this.getHomeData(params);
    });
    this.getCategoryData();
    this.getTagsData();
  }

  ngOnInit(): void {}
  private getHomeData = (page: any) => {
    this.blogService.getBlogList(page).subscribe(
      (data) => {
        this.titleService.setTitle('All Posts | Sing NoteBook');
        this.items = data;
      },
      (error) => {
        console.log(error);
      }
    );
  };

  private getCategoryData = () => {
    this.blogService.getCategories().subscribe(
      (data) => {
        this.categoryData = data;
        this.blogService.changeCategoriesMessage(data);
      },
      (error) => {
        console.log(error);
      }
    );
  };

  private getTagsData = () => {
    this.blogService.getTags().subscribe(
      (data) => {
        this.tagsData = data;
        this.blogService.changeTagsMessage(data);
      },
      (error) => {
        console.log(error);
      }
    );
  };
}
