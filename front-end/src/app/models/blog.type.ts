export interface BlogImg {
  title: string;
  img: string;
}

export interface BlogListItem {
  created_time: string;
  img: BlogImg;
  title: string;
  author: string;
  slug: string;
}

export interface BlogList {
  count: number;
  next: null;
  previous: null;
  results: BlogListItem[];
}

export interface BlogBadges {
  title: string;
  slug: string;
  body: string;
}

export type Keyword = {
  title: string;
  desc: string;
};

export type DetailPage = {
  slug: string;
  title: string;
  status: number;
};

export type BlogDetail = {
  blog: {
    tags: BlogBadges[];
    category: BlogBadges;
    keyword: Keyword;
    img: BlogImg;
    created_time: string;
    title: string;
    body: string;
    author: string;
    slug: string;
    script: string;
  };
  next_page: DetailPage;
  pre_page: DetailPage;
};

export interface BlogQuryset {
  category: string;
  tags: string;
  page: number;
}
