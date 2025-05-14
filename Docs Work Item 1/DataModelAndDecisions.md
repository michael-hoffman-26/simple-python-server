# Truck and Package Data Model

## Table of Contents

1. [Tables Overview](#tables-overview)
   - [Trucks Table](#trucks-table)
   - [Packages Table](#packages-table)
2. [Constraints Overview](#constraints-overview)
   - [Positive Dimensions](#positive-dimensions)
   - [Truck Capacity Management](#truck-capacity-management)
   - [Truck Assignment (One-to-Many)](#truck-assignment-one-to-many)
   - [Delivery Day](#delivery-day)
   - [Fill Percentage](#fill-percentage)
3. [Key Concepts](#key-concepts)
4. [ Error Handling](#error-handling)

---

## Tables Overview

### Trucks Table

This table stores information about each truck and its delivery schedule.

| Field          | Data Type   | Constraint                                                     |
| -------------- | ----------- | -------------------------------------------------------------- |
| `id`           | `INT`       | `PRIMARY KEY`, `AUTO_INCREMENT`                                |
| `length`       | `FLOAT`     | `NOT NULL`, `CHECK(length > 0)`                                |
| `width`        | `FLOAT`     | `NOT NULL`, `CHECK(width > 0)`                                 |
| `height`       | `FLOAT`     | `NOT NULL`, `CHECK(height > 0)`                                |
| `delivery_day` | `DATE`      | `NOT NULL` (The day when this truck is scheduled for delivery) |
| `fill_percentage` |	`FLOAT`	| `NOT NULL`, `DEFAULT 0`, `CHECK(fill_percentage >= 0 AND fill_percentage <= 100)` |
| `created_at`   | `TIMESTAMP` | `DEFAULT CURRENT_TIMESTAMP`                                    |

---

### Packages Table

This table stores information about packages, their dimensions, and their assignment to trucks.

| Field        | Data Type   | Constraint                                                 |
| ------------ | ----------- | ---------------------------------------------------------- |
| `id`         | `INT`       | `PRIMARY KEY`, `AUTO_INCREMENT`                            |
| `length`     | `FLOAT`     | `NOT NULL`, `CHECK(length > 0)`                            |
| `width`      | `FLOAT`     | `NOT NULL`, `CHECK(width > 0)`                             |
| `height`     | `FLOAT`     | `NOT NULL`, `CHECK(height > 0)`                            |
| `truck_id`   | `INT`       | `NULLABLE`, `FOREIGN KEY (truck_id) REFERENCES Trucks(id)` |
| `created_at` | `TIMESTAMP` | `DEFAULT CURRENT_TIMESTAMP`                                |

---


## Constraints Overview

* **Positive Dimensions**:

  * All **length**, **width**, and **height** fields have `CHECK` constraints to ensure they are positive values.

* **Truck Capacity Management**:

  * Truck capacity (the combination of its **length**, **width**, and **height**) determines how much volume can be assigned.
  * Trucks and packages are not automatically marked as full unless logic for checking the volume is explicitly triggered.

* **Truck Assignment (One-to-Many)**:

  * Each **package** can only be assigned to **one truck** at a time, but a truck can have multiple packages.
  * **`truck_id` is nullable** on packages, allowing packages to exist before being assigned.

* **Delivery Day**:

  * **Delivery day** is tied to the truck and is used to manage the shipment date for all packages in the truck.
  * If a package is delayed (unable to be loaded), it is **inferred from the truck’s `delivery_day`**.
  * If a truck has its `delivery_day` set for tomorrow, the **delayed packages** will be scheduled for tomorrow’s delivery.

* **Fill Prcentage**:

  * **fill_percentage** stores the truck’s current load in percentage terms (0 to 100).
---

## Key Concepts

* **Truck-to-Package**: One truck can carry many packages, but each package belongs to only one truck.
* **Delayed Shipments**: A truck with a **`delivery_day`** of tomorrow indicates that packages have been deferred, and the shipment will be processed the next day.
* **Handling Capacity**: If the truck’s current load does not meet the **80% threshold**, the remaining packages are marked for **delay**.

---

Absolutely! Here's a short, clear paragraph you can add to your `README.md` under a new section called **Error Handling**:

---

## Error Handling

The system includes validation and error-handling logic to ensure data integrity and operational stability:

* **Input Validation**: All dimensions (`length`, `width`, `height`) must be positive numbers. Database-level `CHECK` constraints enforce this.
* **Missing or Invalid Fields**: If required fields are missing or invalid in any request (e.g., negative dimensions), the request is rejected with an appropriate error message.
* **Truck Assignment Failures**: If no truck can accommodate the given packages (either due to insufficient capacity or inability to meet the 80% fill threshold), the packages are deferred and scheduled for the next delivery day.
* **Database Constraints**: Foreign key constraints ensure that only valid truck IDs can be assigned to packages, and a package can only be assigned once.

This approach ensures both backend integrity and meaningful feedback for users or calling systems.

---

