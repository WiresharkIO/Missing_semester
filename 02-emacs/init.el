;; NOTE: init.el is now generated from Emacs.org.  Please edit that file
;;       in Emacs and init.el will be generated automatically!

(defun efs/display-startup-time ()
  (message "Emacs loaded in %s with %d garbage collections."
           (format "%.2f seconds"
                   (float-time
                     (time-subtract after-init-time before-init-time)))
           gcs-done))

(add-hook 'emacs-startup-hook #'efs/display-startup-time)

;; Initialize package sources
(require 'package)
(add-to-list 'package-archives '("melpa" . "https://melpa.org/packages/") t)
(package-initialize)

;; Make ESC quit prompts
(global-set-key (kbd "<escape>") 'keyboard-escape-quit)

(use-package command-log-mode
  :commands command-log-mode)

(use-package spacemacs-theme
  :ensure t
  :init (load-theme 'spacemacs-dark t))
  
;; Install use-package (if not already installed)
(unless (package-installed-p 'use-package)
  (package-refresh-contents)
  (package-install 'use-package))
(use-package python-mode :ensure t)

;; Configure use-package
(eval-when-compile
  (require 'use-package))
(setq use-package-always-ensure t)

;; Python mode
(use-package python-mode
  :mode ("\\.py\\'" . python-mode)
  :interpreter ("python" . python-mode)
  :config
  (setq python-shell-interpreter "python3"))

;; Enable syntax highlighting
(global-font-lock-mode t)

;; Set indentation style
(setq-default indent-tabs-mode nil) ; Use spaces for indentation
(setq-default tab-width 4)          ; Set default tab width to 4 spaces

;; Enable auto-completion with company-mode
(use-package company
  :config
  (add-hook 'python-mode-hook 'company-mode))

;; Enable linting with flycheck
(use-package flycheck
  :config
  (add-hook 'python-mode-hook 'flycheck-mode))

;; Enable code formatting with black (Python formatter)
(use-package blacken
  :config
  (add-hook 'python-mode-hook 'blacken-mode))

(setq markdown-command "/usr/bin/pandoc")

(use-package magit
  :commands magit-status
  :custom
  (magit-display-buffer-function #'magit-display-buffer-same-window-except-diff-v1))
