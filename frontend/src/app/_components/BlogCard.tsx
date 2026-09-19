import Image from "next/image";

export default function BlogCard({ post }: { post: any }) {
  return (
    <div className="flex flex-col gap-4">
      <h2 className="text-2xl font-bold">{post.title}</h2>
      <p className="text-sm text-gray-500">{post.description}</p>
      <p className="text-sm text-gray-500">{post.content}</p>
      <p className="text-sm text-gray-500">{post.created_at}</p>
      <p className="text-sm text-gray-500">{post.updated_at}</p>
      <p className="text-sm text-gray-500">{post.author}</p>
      <p className="text-sm text-gray-500">{post.category}</p>
    </div>
  );
}
