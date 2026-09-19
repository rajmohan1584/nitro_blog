import Image from "next/image";

export default function TitleBar() {
  return (
    <header className="flex w-full items-center justify-between border-b border-zinc-200 bg-white px-6 py-3">
      {/* Left */}
      <div className="flex items-center gap-3">
        <Image
          src="/assets/nitro-logo.png"
          alt="Nitro"
          width={40}
          height={40}
        />

        <span className="text-xl font-semibold text-zinc-900">
          Nitro Blog
        </span>
      </div>

      {/* Right */}
      <div className="flex items-center gap-3">
        <button className="rounded-md px-4 py-2 text-sm font-medium text-zinc-700 hover:bg-zinc-100">
          Login
        </button>

        <button className="rounded-md bg-zinc-900 px-4 py-2 text-sm font-medium text-white hover:bg-zinc-700">
          Register
        </button>
      </div>
    </header>
  );
}
