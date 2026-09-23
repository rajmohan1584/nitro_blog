import Image from "next/image";
import { useRouter } from "next/navigation";
import "./BlogCard.css";
import Button from "@/components/Button";

export default function BlogCard({ post }: { post: any }) {
  const router = useRouter();
  return (
    <div className="blog-card">
      {/* Header */}
      <div className="blog-card-header" onClick={() => router.push(`/posts/${post.id}`)}>
        {post.title}
      </div>

      {/* Body */}
      <div className="blog-card-body">{post.content}</div>

      {/* Footer */}
      <div className="blog-card-footer">
        <Image
          src="http://localhost:8000/static/nitro-logo.png"
          alt={post.author?.username ?? "Author"}
          width={40}
          height={40}
          className="rounded-full object-cover"
        />
        {post.author?.username}
        <Button text="Edit" variant="primary" className="ml-2" />
        <Button text="Delete" variant="danger" className="ml-2" />
      </div>
    </div>
  );
}
