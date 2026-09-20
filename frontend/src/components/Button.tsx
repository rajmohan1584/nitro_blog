interface ButtonProps {
  onClick?: () => void;
  text: string;
}

export default function Button({ onClick, text }: ButtonProps) {
  return (
    <button
          onClick={onClick}
          className="rounded-md px-4 py-2 text-sm text-zinc-700 hover:bg-zinc-100 dark:text-zinc-200 dark:hover:bg-zinc-800"
        >
          {text}
        </button>
  );
}
