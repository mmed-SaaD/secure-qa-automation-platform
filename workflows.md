## 1 - Authentication workflow

Open login → fill credentials → submit → land on Products

Positive login (standard_user)

Negative login (wrong user/pass)

Locked user login (locked_out_user)

Logout workflow (menu → logout → back to login)

## 2 - Browse Products workflow

Login → view products list → open product details → back to list

Verify products list loads

Open random item details

Validate item details match list (name/price)

## 3 - Sorting workflow

Login → products → change sort → verify ordering

Sort by Name A→Z

Sort by Name Z→A

Sort by Price low→high

Sort by Price high→low

## 4 - Cart management workflow

Login → add item(s) → cart → update cart

Add one item from list

Add one item from details page

Remove item from list

Remove item from cart

Verify cart badge count updates

## 5 - Checkout workflow (happy path)

Login → add items → cart → checkout → info → overview → finish

Fill checkout info (first/last/zip)

Verify overview totals (item total, tax, total)

Complete checkout (Finish)

Verify “Thank you” / complete page

Back Home returns to products

## 6 - Checkout workflow (negative/validation)

Checkout → submit missing info → error shown

Missing first name

Missing last name

Missing postal code

## 7- Session / State workflow

Refresh page retains cart count

Open new tab/session behavior (optional)

Logout clears session (after logout, opening /inventory should redirect to login)