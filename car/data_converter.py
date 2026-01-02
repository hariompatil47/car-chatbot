import pandas as pd
from langchain_core.documents import Document


class DataConverter:
    def __init__(self, file_path: str):
        self.file_path = file_path

    def convert(self):
        sheets = pd.read_excel(self.file_path, sheet_name=None)
        docs = []

        for name, df in sheets.items():
            name = name.lower()

            # -------- MAKES --------
            if name == "Makes":
                for _, r in df.iterrows():
                    content = (
                        f"Type: Make\n"
                        f"Make Id: {r['Make Id']}\n"
                        f"Make Name: {r['Make Name']}\n"
                        f"Make Created: {r['Make Created']}\n"
                        f"Make Modified: {r['Make Modified']}"
                    )

                    docs.append(
                        Document(
                            page_content=content,
                            metadata={
                                "type": "make",
                                "make_id": r["Make Id"],
                                "make_name": r["Make Name"],
                            },
                        )
                    )

            # -------- MODELS --------
            elif name == "Models":
                for _, r in df.iterrows():
                    content = (
                        f"Type: Model\n"
                        f"Make Id: {r['Make Id']}\n"
                        f"Model Id: {r['Model Id']}\n"
                        f"Model Year: {r['Model Year']}\n"
                        f"Make Name: {r['Make Name']}\n"
                        f"Model Name: {r['Model Name']}\n"
                        f"Model Created: {r['Model Created']}\n"
                        f"Model Modified: {r['Model Modified']}"
                    )

                    docs.append(
                        Document(
                            page_content=content,
                            metadata={
                                "type": "model",
                                "model_id": r["Model Id"],
                                "make": r["Make Name"],
                                "year": r["Model Year"],
                            },
                        )
                    )

            # -------- SUBMODELS --------
            elif name == "Submodels":
                for _, r in df.iterrows():
                    content = (
                        f"Type: Submodel\n"
                        f"Make Id: {r['Make Id']}\n"
                        f"Model Id: {r['Model Id']}\n"
                        f"Submodel Id: {r['Submodel Id']}\n"
                        f"Model Year: {r['Model Year']}\n"
                        f"Make Name: {r['Make Name']}\n"
                        f"Model Name: {r['Model Name']}\n"
                        f"Submodel Name: {r['Submodel Name']}\n"
                        f"Submodel Created: {r['Submodel Created']}\n"
                        f"Submodel Modified: {r['Submodel Modified']}"
                    )

                    docs.append(
                        Document(
                            page_content=content,
                            metadata={
                                "type": "submodel",
                                "submodel_id": r["Submodel Id"],
                                "model_id": r["Model Id"],
                            },
                        )
                    )

            # -------- TRIMS --------
            elif name == "Trims":
                for _, r in df.iterrows():
                    content = (
                        f"Type: Trim\n"
                        f"Make Id: {r['Make Id']}\n"
                        f"Model Id: {r['Model Id']}\n"
                        f"Submodel Id: {r['Submodel Id']}\n"
                        f"Trim Id: {r['Trim Id']}\n"
                        f"Model Year: {r['Model Year']}\n"
                        f"Make Name: {r['Make Name']}\n"
                        f"Model Name: {r['Model Name']}\n"
                        f"Submodel Name: {r['Submodel Name']}\n"
                        f"Trim Name: {r['Trim Name']}\n"
                        f"Trim Description: {r['Trim Description']}\n"
                        f"Trim MSRP: {r['Trim MSRP']}\n"
                        f"Trim Invoice: {r['Trim Invoice']}\n"
                        f"Trim Created: {r['Trim Created']}\n"
                        f"Trim Modified: {r['Trim Modified']}"
                    )

                    docs.append(
                        Document(
                            page_content=content,
                            metadata={
                                "type": "trim",
                                "trim_id": r["Trim Id"],
                                "model_id": r["Model Id"],
                            },
                        )
                    )

            # -------- BODIES --------
            elif name == "Bodies":
                for _, r in df.iterrows():
                    content = (
                        f"Type: Body\n"
                        f"Make Id: {r['Make Id']}\n"
                        f"Model Id: {r['Model Id']}\n"
                        f"Submodel Id: {r['Submodel Id']}\n"
                        f"Trim Id: {r['Trim Id']}\n"
                        f"Body Id: {r['Body Id']}\n"
                        f"Model Year: {r['Model Year']}\n"
                        f"Make Name: {r['Make Name']}\n"
                        f"Model Name: {r['Model Name']}\n"
                        f"Submodel Name: {r['Submodel Name']}\n"
                        f"Trim Name: {r['Trim Name']}\n"
                        f"Body Type: {r['Body Type']}\n"
                        f"Body Doors: {r['Body Doors']}\n"
                        f"Body Seats: {r['Body Seats']}\n"
                        f"Body Created: {r['Body Created']}\n"
                        f"Body Modified: {r['Body Modified']}"
                    )

                    docs.append(
                        Document(
                            page_content=content,
                            metadata={
                                "type": "body",
                                "body_id": r["Body Id"],
                                "trim_id": r["Trim Id"],
                            },
                        )
                    )

            # -------- ENGINES --------
            elif name == "Engines":
                for _, r in df.iterrows():
                    content = (
                        f"Type: Engine\n"
                        f"Engine Id: {r['Engine Id']}\n"
                        f"Make Id: {r['Make Id']}\n"
                        f"Model Id: {r['Model Id']}\n"
                        f"Trim Id: {r['Trim Id']}\n"
                        f"Model Year: {r['Model Year']}\n"
                        f"Engine Name: {r['Engine Type']}\n"
                        f"Engine Fuel Type: {r['Engine Fuel Type']}\n"
                        f"Engine Cylinders: {r['Engine Cylinders']}\n"
                        f"Engine Horsepower: {r['Engine Horsepower Hp']}\n"
                        f"Engine Transmission: {r['Engine Transmission']}\n"
                        f"Engine Created: {r['Engine Created']}\n"
                        f"Engine Modified: {r['Engine Modified']}"
                    )

                    docs.append(
                        Document(
                            page_content=content,
                            metadata={
                                "type": "engine",
                                "engine_id": r["Engine Id"],
                                "model_id": r["Model Id"],
                            },
                        )
                    )

            # -------- MILEAGES --------
            elif name == "Mileages":
                for _, r in df.iterrows():
                    content = (
                        f"Type: Mileage\n"
                        f"Mileage Id: {r['Mileage Id']}\n"
                        f"Model Id: {r['Model Id']}\n"
                        f"Trim Id: {r['Trim Id']}\n"
                        f"Model Year: {r['Model Year']}\n"
                        f"Mileage Combined Mpg: {r['Mileage Combined Mpg']}\n"
                        f"Mileage Epa City Mpg: {r['Mileage Epa City Mpg']}\n"
                        f"Mileage Epa Highway Mpg: {r['Mileage Epa Highway Mpg']}\n"
                        f"Mileage Created: {r['Mileage Created']}\n"
                        f"Mileage Modified: {r['Mileage Modified']}"
                    )

                    docs.append(
                        Document(
                            page_content=content,
                            metadata={
                                "type": "mileage",
                                "mileage_id": r["Mileage Id"],
                                "model_id": r["Model Id"],
                            },
                        )
                    )

        return docs
