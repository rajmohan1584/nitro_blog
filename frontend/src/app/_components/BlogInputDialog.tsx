"use client";

import { useState } from "react";
import Button from "@/components/Button";
import "./BlogInputDialog.css";

interface BlogInputDialogProps {
  post: { title: string; content: string };
  onOk: (updated: { title: string; content: string }) => void;
  onCancel: () => void;
}

export default function BlogInputDialog({ post, onOk, onCancel }: BlogInputDialogProps) {
  const [title, setTitle] = useState(post.title);
  const [content, setContent] = useState(post.content);

  const canSave = title.trim().length > 0 && content.trim().length > 0;

  return (
    <div className="blog-input-dialog-overlay">
      <div className="blog-input-dialog">
        <div className="blog-input-dialog-title">Edit Post</div>

        <div className="blog-input-dialog-body">
          <label className="blog-input-dialog-label" htmlFor="blog-input-title">
            Title
          </label>
          <input
            id="blog-input-title"
            className="blog-input-dialog-input"
            value={title}
            onChange={(e) => setTitle(e.target.value)}
          />

          <label className="blog-input-dialog-label" htmlFor="blog-input-content">
            Content
          </label>
          <textarea
            id="blog-input-content"
            className="blog-input-dialog-textarea"
            value={content}
            onChange={(e) => setContent(e.target.value)}
            rows={6}
          />
        </div>

        <div className="blog-input-dialog-footer">
          <Button text="Cancel" onClick={onCancel} variant="default" />
          <Button
            text="OK"
            variant="primary"
            onClick={() => canSave && onOk({ title: title.trim(), content: content.trim() })}
          />
        </div>
      </div>
    </div>
  );
}
