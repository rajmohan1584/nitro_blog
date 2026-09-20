"use client";
import Image from "next/image";
import { useRouter } from "next/navigation";
import { useTheme } from "@/providers/ThemeProvider";
import Button from "./Button";

export default function TitleBar() {
  const { theme, toggleTheme } = useTheme();
  const router = useRouter();

  return (
    <header
      className="flex w-full items-center justify-between 
                 border-b border-zinc-200 bg-white dark:bg-zinc-900 dark:border-zinc-800 
                 px-6 py-3 text-zinc-900 dark:text-zinc-100">
      {/* Left */}
      <div className="flex items-center gap-3">
        <Image
          src="/assets/nitro-logo.png"
          alt="Nitro"
          width={40}
          height={40}
        />

        <span className="text-xl font-semibold">
          Nitro Blog
        </span>

        <Button text="Home" onClick={() => router.push("/")} />
      </div>

      {/* Right */}
      <div className="flex items-center gap-3">
        <Button text={theme === "light" ? "Dark" : "Light"} onClick={toggleTheme} />
        <Button text="Login" onClick={() => {}} />
        <Button text="Register" onClick={() => {}} />
      </div>
    </header>
  );
}
