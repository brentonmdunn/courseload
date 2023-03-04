import Head from "next/head";
import {
  Key,
  ReactElement,
  JSXElementConstructor,
  ReactFragment,
  ReactPortal,
} from "react";

const fetchjson = (props: any) => {
  const posts = props.posts;
  return (
    <div style={{ padding: 30 }}>
      <Head>
        <title>Sling Academy</title>
      </Head>
      <div>
        {posts.map((post: any) => (
          <div
            key={post.id}
            style={{ padding: 20, borderBottom: "1px solid #ccc" }}
          >
            <h2>{post.title}</h2>
            <p>{post.content}</p>
          </div>
        ))}
      </div>
    </div>
  );
};

import fsPromises from "fs/promises";
import path from "path";
export async function getStaticProps() {
  const filePath = path.join(process.cwd(), "data.json");
  const jsonData = await fsPromises.readFile(filePath);
  const objectData = JSON.parse(jsonData.toString());

  return {
    props: objectData,
  };
}

export default fetchjson;
