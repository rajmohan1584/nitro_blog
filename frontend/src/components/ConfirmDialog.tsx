"use client";

import "./ConfirmDialog.css";

interface ConfirmDialogProps {
  title?: string;
  message?: string;
  okText?: string;
  cancelText?: string;
  onOk: () => void;
  onCancel: () => void;
}

export default function ConfirmDialog({
  title = "Confirm",
  message = "Are you sure?",
  okText = "OK",
  cancelText = "Cancel",
  onOk,
  onCancel,
}: ConfirmDialogProps) {
  return (
    <div className="confirm-dialog-overlay">
      <div className="confirm-dialog">
        <div className="confirm-dialog-title">{title}</div>

        <div className="confirm-dialog-body">{message}</div>

        <div className="confirm-dialog-footer">
          <button className="confirm-dialog-cancel" onClick={onCancel}>
            {cancelText}
          </button>

          <button className="confirm-dialog-ok" onClick={onOk}>
            {okText}
          </button>
        </div>
      </div>
    </div>
  );
}
