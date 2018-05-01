import sqlalchemy
import cubes
import cubes.tutorial.sql as tutorial

engine = sqlalchemy.create_engine('sqlite:///:memory:')
tutorial.create_table_from_csv(engine,
                      "IBRD_Balance_Sheet__FY2010.csv",
                      table_name="irbd_balance",
                      fields=[
                            ("category", "string"),
                            ("line_item", "string"),
                            ("year", "integer"),
                            ("amount", "integer")],
                      create_id=True

                        )


model = cubes.Model
model.add_dimension(cubes.Dimension("category"))
model.add_dimension(cubes.Dimension("line_item"))
model.add_dimension(cubes.Dimension("year"))

cube = cubes.Cube(name="irbd_balance",
                  model=model,
                  dimensions=["category", "line_item", "year"],
                  measures=["amount"]
                  )

browser = cubes.backends.sql.SQLBrowser(cube, engine.connect(), view_name = "irbd_balance")

cell = browser.full_cube()
result = browser.aggregate(cell)

print( "Record count: %d" % result.summary["record_count"])
print ("Total amount: %d" % result.summary["amount_sum"])