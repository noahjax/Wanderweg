const TransportPlannerParent = require("./TransportPlannerParent")
// @ponicode
describe("componentDidMount", () => {
    let inst

    beforeEach(() => {
        inst = new TransportPlannerParent.default()
    })

    test("0", () => {
        let callFunction = () => {
            inst.componentDidMount()
        }
    
        expect(callFunction).not.toThrow()
    })
})

// @ponicode
describe("fetch", () => {
    let inst

    beforeEach(() => {
        inst = new TransportPlannerParent.default()
    })

    test("0", () => {
        let callFunction = () => {
            inst.fetch()
        }
    
        expect(callFunction).not.toThrow()
    })
})
