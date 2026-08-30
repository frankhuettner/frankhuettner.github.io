import rss from "@astrojs/rss";
import { getCollection } from "astro:content";
import type { APIContext } from "astro";

export async function GET(context: APIContext) {
  const news = (await getCollection("news")).sort((a, b) => b.data.date.valueOf() - a.data.date.valueOf());

  return rss({
    title: "Frank Huettner — news",
    description: "Announcements and updates from Frank Huettner.",
    site: context.site!,
    items: news.map((item) => ({
      title: item.body?.trim().slice(0, 90).replace(/\s+\S*$/, "") ?? item.id,
      pubDate: item.data.date,
      link: `/news/#${item.id}`,
      content: item.body ?? "",
    })),
  });
}
