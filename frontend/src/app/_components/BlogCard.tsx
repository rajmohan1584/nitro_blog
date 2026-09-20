// import Image from "next/image";
import "./BlogCard.css";

export default function BlogCard({ post }: { post: any }) {
  return (
    <div
      className="blog-card">

      {/* Header */}
      <div className="blog-card-header">
        {post.title}
      </div>


      {/* Body */}
      <div className="blog-card-body">
        {post.content}
      </div>


      {/* Footer */}
      <div className="blog-card-footer">
        {post.author}
      </div>

    </div>
  );
}
