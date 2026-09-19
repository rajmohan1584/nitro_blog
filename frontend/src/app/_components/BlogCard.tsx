import Image from "next/image";

export default function BlogCard({ post }: { post: any }) {
  return (
    <div className="flex h-[300px] w-full flex-col overflow-hidden rounded-lg shadow-md border border-zinc-200">

      {/* Header */}
      <div className="border-b border-zinc-200 px-4 py-3">{post.title}</div>


      {/* Body */}
      <div className="flex-1 px-4 py-3 text-sm text-zinc-600">{post.content}</div>


      {/* Footer */}
      <div className="border-t border-zinc-200 px-4 py-2 text-xs text-zinc-500">{post.author}</div>

    </div>
  );
}
