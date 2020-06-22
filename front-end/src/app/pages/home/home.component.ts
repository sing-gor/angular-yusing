import { Component, OnInit } from '@angular/core';
import { BlogHandlerService } from 'src/app/services/blog-handler.service';
import { Title } from '@angular/platform-browser';
import { BlogList, BlogListItem, BlogBadges } from 'src/app/models/blog.type';
@Component({
  selector: 'app-home',
  templateUrl: './home.component.html',
  styleUrls: ['./home.component.less'],
})
export class HomeComponent implements OnInit {
  public pageIndexs: number;
  public items: BlogList;
  public categoryData: BlogBadges[];
  public tagsData: BlogBadges[];
  constructor(
    private blogService: BlogHandlerService,
    private titleService: Title
  ) {
    this.getHomeData();
    this.getCategoryData();
    this.getTagsData();
  }

  ngOnInit(): void {}

  private getHomeData = () => {
    let pages = {};
    this.blogService.getBlogList(pages).subscribe(
      (data) => {
        this.titleService.setTitle('Home | Sing NoteBook');
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
