"use client";

import { useEffect, useState } from "react";
import TitleBar from "../components/TitleBar";
import BlogCard from "./_components/BlogCard";

export default function Home() {
  const [data, setData] = useState([]);
  useEffect(() => {
    fetch("http://localhost:8000/posts")
      .then((res) => res.json())
      .then((data) => setData(data))
      .catch((err) => console.error("Fetch failed:", err));
  }, []);
  console.log(data);
  
  return (
    <>
      <TitleBar />
      <main>
        {data.map((post: any) => (
          <BlogCard key={post.id} post={post} />
        ))}
      </main>
    </>
  );
}
