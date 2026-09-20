import Image from "next/image";

export default function BlogCard({ post }: { post: any }) {
  return (
    <div
      className="flex h-75 w-full flex-col overflow-hidden rounded-lg shadow-md border 
                 border-zinc-200 bg-white text-zinc-900
                 dark:border-zinc-800 dark:bg-zinc-900 dark:text-zinc-100">

      {/* Header */}
      <div className="border-b  px-4 py-3
                      border-zinc-200
                      dark:border-zinc-800">
        {post.title}
      </div>


      {/* Body */}
      <div className="flex-1 px-4 py-3 text-sm 
                      text-zinc-600
                      dark:text-zinc-400">
        {post.content}
      </div>


      {/* Footer */}
      <div className="border-t px-4 py-2 text-xs
                      border-zinc-200 text-zinc-500
                      dark:border-zinc-800 dark:text-zinc-400">
        {post.author}
      </div>

    </div>
  );
}
