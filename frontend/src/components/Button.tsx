"use client";

type Variant = "default" | "primary" | "danger";

interface ButtonProps {
  onClick?: () => void;
  text: string;
  className?: string;
  variant?: Variant;
}

const variants: Record<Variant, string> = {
  default:
    "text-zinc-700 hover:bg-zinc-100 dark:text-zinc-200 dark:hover:bg-zinc-800",
  primary:
    "border border-blue-500 text-blue-500 hover:bg-blue-500 hover:text-white",
  danger:
    "border border-red-500 text-red-500 hover:bg-red-500 hover:text-white",
};

export default function Button({
  onClick,
  text,
  className = "",
  variant = "default",
}: ButtonProps) {
  return (
    <button
      onClick={onClick}
      className={`rounded-md px-4 py-2 text-sm ${variants[variant]} ${className}`}
    >
      {text}
    </button>
  );
}
