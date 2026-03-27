import rss from '@astrojs/rss';
import { getCollection } from 'astro:content';

export async function GET(context: import('astro').APIContext) {
  const blog = await getCollection('blog');
  const sortedPosts = blog.sort(
    (a, b) => b.data.pubDate.valueOf() - a.data.pubDate.valueOf()
  );

  return rss({
    title: 'Swarm Notes RSS Feed',
    description: 'Articles, tutorials, and updates from the Swarm Notes project',
    site: context.site ?? 'https://swarm-notes.kausalflow.com',
    items: sortedPosts.map((post) => ({
      title: post.data.title,
      pubDate: post.data.pubDate,
      description: post.data.description,
      author: post.data.author,
      link: `/blog/${post.id}/`,
    })),
    customData: `<language>en-us</language>`,
  });
}
