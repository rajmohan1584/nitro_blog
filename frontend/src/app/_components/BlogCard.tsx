import Image from "next/image";
import { useRouter } from "next/navigation";
import "./BlogCard.css";
import Button from "@/components/Button";
import { useState } from "react";
import ConfirmDialog from "@/components/ConfirmDialog";
import BlogInputDialog from "./BlogInputDialog";

export default function BlogCard({ post }: { post: any }) {
  const [showDeleteDialog, setShowDeleteDialog] = useState(false);
  const [showEditDialog, setShowEditDialog] = useState(false);
  const router = useRouter();

  const handleSave = (post: any) => {
    console.log(post);
    setShowEditDialog(false);
  };

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
        <Button text="Edit" variant="primary" className="ml-2" onClick={() => setShowEditDialog(true)} />
        <Button text="Delete" variant="danger" className="ml-2" onClick={() => setShowDeleteDialog(true)} />
      </div>
      {showDeleteDialog && <ConfirmDialog onOk={() => {}} onCancel={() => setShowDeleteDialog(false)} />}
      {showEditDialog && (
        <BlogInputDialog post={post} onOk={(post: any) => handleSave(post)} onCancel={() => setShowEditDialog(false)} />
      )}
    </div>
  );
}
